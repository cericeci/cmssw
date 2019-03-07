/*
 * PdfModuleWithStats.cc
 *
 *  Created on: Feb 4, 2019
 *      Author: Karol Bunkowski kbunkow@cern.ch
 */

#include "L1Trigger/L1TMuonBayes/interface/MuCorrelator/PdfModuleWithStats.h"

#include "TFitResultPtr.h"
#include "TFitResult.h"
#include "TF1.h"

PdfModuleWithStats::PdfModuleWithStats(MuCorrelatorConfigPtr& config): PdfModule(config), pdfHists(config->nLayers() ) {
  TFileDirectory subDir = fs->mkdir("pdfs");

  for(unsigned int iLayer = 0; iLayer < coefficients.size(); ++iLayer) {
    for(unsigned int iEtaBin = 0; iEtaBin < coefficients[iLayer].size(); ++iEtaBin) {
      pdfHists[iLayer].emplace_back();
      for(unsigned int iRefLayer = 0; iRefLayer < coefficients[iLayer][iEtaBin].size(); ++iRefLayer) {
        std::ostringstream name;
                name<<"pdfHist_layer_"<<iLayer<<"_eta_"<<iEtaBin<<"_refLayer_"<<iRefLayer;
        pdfHists[iLayer][iEtaBin].emplace_back(subDir.make<TH2I>(name.str(). c_str(), name.str(). c_str(),
                                                           config->nPtBins(), 0, config->nPtBins(), 1300, -100 -0.5, 1200 -0.5));
      }
    }

    //[layer][etaBin][refLayer](ptBin, pdfBin)
  }
}

PdfModuleWithStats::~PdfModuleWithStats() {
  // TODO Auto-generated destructor stub
}

float PdfModuleWithStats::getPdfVal(unsigned int layer, unsigned int etaBin, unsigned int refLayer, unsigned int ptBin, int pdfBin) {
  pdfHists.at(layer).at(etaBin).at(refLayer)->Fill(ptBin, pdfBin);
  return PdfModule::getPdfVal(layer, etaBin, refLayer, ptBin, pdfBin);
}

/* whith file service it is not needed
void PdfModuleWithStats::write() const {
  for(unsigned int iLayer = 0; iLayer < pdfHists.size(); ++iLayer) {
    for(unsigned int iEtaBin = 0; iEtaBin < pdfHists[iLayer].size(); ++iEtaBin) {
      for(unsigned int iRefLayer = 0; iRefLayer < pdfHists[iLayer][iEtaBin].size(); ++iRefLayer) {
        pdfHists.at(iLayer).at(iEtaBin).at(iRefLayer)->Write();
      }
    }
  }
}*/

//The pdfs coefficients are generated by calculating the mean and sigma, and not by fitting parabola (since fit often fails or is not accurate)
void PdfModuleWithStats::generateCoefficients() {
  //fs->cd();
  TFileDirectory subDir = fs->mkdir("pdfsProj"); //does not work, why?
  //subDir.cd();

  for(unsigned int iLayer = 0; iLayer < pdfHists.size(); ++iLayer) {
    for(unsigned int iEtaBin = 0; iEtaBin < pdfHists[iLayer].size(); ++iEtaBin) {
      for(unsigned int iRefLayer = 0; iRefLayer < pdfHists[iLayer][iEtaBin].size(); ++iRefLayer) {
        auto pdfHist = pdfHists.at(iLayer).at(iEtaBin).at(iRefLayer);
        for(int ptBin = 0; ptBin < pdfHist->GetXaxis()->GetNbins(); ++ptBin) {
          //clean the old values
          coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(2) = 0;
          coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(1) = 0;
          coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(0) = 0;

          //Normalize pdf in each ptBin separately, to get p(pdBin | pt, eta)
          std::ostringstream ostr;
          ostr<<pdfHist->GetName()<<"_ptBin_"<<ptBin;
          TH1D* pdfHistInPtBin = pdfHist->ProjectionY(ostr.str().c_str(), ptBin +1, ptBin +1); //+1 Because the bins in root hist are counted from 1
          ostr<<" "<<config->ptBinString(ptBin, 1);
          pdfHistInPtBin->SetTitle(ostr.str().c_str());

          pdfHistInPtBin->Sumw2();
          if(pdfHistInPtBin->Integral() <= 0) {
            std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin<<" - no entries, coefficients not calculated"<<std::endl;
            continue;
          }

          pdfHistInPtBin->Scale(1./pdfHistInPtBin->Integral());

          const double minPlog =  log(config->minPdfVal());
          const double pdfMaxLogVal = config->pdfMaxLogValue();

          //removing points with small statiscticas before calculating mean and sigma
          int notEmtyBins = 0;
          for(int iBinPdf = 0; iBinPdf < pdfHistInPtBin->GetXaxis()->GetNbins(); iBinPdf++) {
            double pdfVal = pdfHistInPtBin->GetBinContent(iBinPdf);

            if( (ptBin <= 16 && pdfVal < config->minPdfVal()) || (ptBin > 16 && pdfVal < config->minPdfVal() *2))  //removing points with small statistics - TODO tune
            {
              pdfHistInPtBin->SetBinContent(iBinPdf, 0);
              pdfHistInPtBin->SetBinError(iBinPdf, 0);
            }
            else
              notEmtyBins++;

          }

          if(ptBin < 5 && notEmtyBins < 10) {
            std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin<<" - notEmtyBins < 10, coefficients not calculated"<<std::endl;
              continue;
          }

          double mean = pdfHistInPtBin->GetMean();
          double sigma = pdfHistInPtBin->GetStdDev();

          //just to ahve the drown histogram, it not needed for the actual coefficients calcucation
          for(int iBinPdf = 0; iBinPdf < pdfHistInPtBin->GetXaxis()->GetNbins(); iBinPdf++) {
            double pdfVal = pdfHistInPtBin->GetBinContent(iBinPdf);

            double logPdf = 0;
            double error = 0;
            if(pdfVal >= config->minPdfVal())  //10 is for removing points with small statistics - TODO tune
            //if(pdfVal > 0)
            {
              logPdf = pdfMaxLogVal - log(pdfVal) * pdfMaxLogVal / minPlog;

              error = -1./pdfVal / minPlog * pdfMaxLogVal * pdfHistInPtBin->GetBinError(iBinPdf);
              error = abs(error);

              /*if(error > 100) { //TODO optimize cut
                logPdf = 0;
                error = 0;
              }*/

            }

            pdfHistInPtBin->SetBinContent(iBinPdf, logPdf);
            pdfHistInPtBin->SetBinError(iBinPdf, error);
          }


          if(sigma != 0) {
            double a = 1./(2. * sigma * sigma) * pdfMaxLogVal / minPlog;
            double b = mean;
            double c = pdfMaxLogVal - log(1./(sigma * sqrt(2*M_PI)) ) * pdfMaxLogVal / minPlog;

            std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                <<" sigma "<<std::setw(10)<<sigma<<" a "<<std::setw(10)<<a<<" b "<<std::setw(10)<<b<<" c "<<std::setw(10)<<c<<std::endl;


            a = round(-a * (1 <<bitShift) );
            b = round(b);
            c = round(c);

            if(a == 0) {
              c = 0;
              std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                                                            <<" a is zero, setting c to 0 as well "<<std::endl;
            }

            std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                <<" sigma "<<std::setw(10)<<sigma<<" a "<<std::setw(10)<<a<<" b "<<std::setw(10)<<b<<" c "<<std::setw(10)<<c<<std::endl;


            TF1* intFit = new TF1("intFit","[2]*(x-[1])*(x-[1])+[0]", -100, 1200);

            intFit->SetParameter(2, (-1) * a / (1<<bitShift));
            intFit->SetParameter(1, b);
            intFit->SetParameter(0, c);

            coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(2) = a;
            coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(1) = b;
            coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(0) = c;


            intFit->SetLineColor(kGreen);
            pdfHistInPtBin->GetListOfFunctions()->Add(intFit);
          }
          else {
            std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                <<" sigma = 0 !!!!!!!!!!! mean = "<<mean<<std::endl;
          }

          pdfHistInPtBin->Write();
        }
      }
    }
  }
}

//THis is not good method, since fit often fails or is not accurate
void PdfModuleWithStats::generateCoefficients1() {
  //fs->cd();
  TFileDirectory subDir = fs->mkdir("pdfsProj"); //does not work, why?
  //subDir.cd();

  for(unsigned int iLayer = 0; iLayer < pdfHists.size(); ++iLayer) {
    for(unsigned int iEtaBin = 0; iEtaBin < pdfHists[iLayer].size(); ++iEtaBin) {
      for(unsigned int iRefLayer = 0; iRefLayer < pdfHists[iLayer][iEtaBin].size(); ++iRefLayer) {
        auto pdfHist = pdfHists.at(iLayer).at(iEtaBin).at(iRefLayer);
        for(int ptBin = 0; ptBin < pdfHist->GetXaxis()->GetNbins(); ++ptBin) {
          //clean the old values
          coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(2) = 0;
          coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(1) = 0;
          coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(0) = 0;

          //Normalize pdf in each ptBin separately, to get p(pdBin | pt, eta)
          std::ostringstream ostr;
          ostr<<pdfHist->GetName()<<"_ptBin_"<<ptBin;
          TH1D* pdfHistInPtBin = pdfHist->ProjectionY(ostr.str().c_str(), ptBin +1, ptBin +1); //+1 Because the bins in root hist are counted from 1
          pdfHistInPtBin->SetTitle(ostr.str().c_str());

          pdfHistInPtBin->Sumw2();
          if(pdfHistInPtBin->Integral() <= 0) {
            std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin<<" - no entries, coefficients not calculated"<<std::endl;
            continue;
          }

          pdfHistInPtBin->Scale(1./pdfHistInPtBin->Integral());

          //pdfHistInPtBin->Write(); //TODO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,,
          //          continue;

          for(int iBinPdf = 0; iBinPdf < pdfHistInPtBin->GetXaxis()->GetNbins(); iBinPdf++) {
            double pdfVal = pdfHistInPtBin->GetBinContent(iBinPdf);

            const double minPlog =  log(config->minPdfVal());
            const double pdfMaxLogVal = config->pdfMaxLogValue();

            double logPdf = 0;
            double error = 0;
            if(pdfVal >= config->minPdfVal()/2.)  //10 is for removing points with small statistics - TODO tune
            //if(pdfVal > 0)
            {
              logPdf = pdfMaxLogVal - log(pdfVal) / minPlog * pdfMaxLogVal;

              error = -1./pdfVal / minPlog * pdfMaxLogVal * pdfHistInPtBin->GetBinError(iBinPdf);
              error = abs(error);

              if(error > 100) { //TODO optimize cut
                logPdf = 0;
                error = 0;
              }

            }

            pdfHistInPtBin->SetBinContent(iBinPdf, logPdf);
            pdfHistInPtBin->SetBinError(iBinPdf, error);
          }

          try {
            TFitResultPtr fitResult = pdfHistInPtBin->Fit("pol2","S");
            Int_t fitStatus = fitResult;
            if(fitStatus == 0) {
              //fitResult->Clear(); is this needed?

              if(fitResult->Chi2() > 1000) { //TODO tune
                std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                                                <<" - chi2 > 1000 - fit failed!!!!!!!!!!!!!!!!!! "<<std::endl;
                pdfHistInPtBin->Write();
                continue; //<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
              }

              double a0 = fitResult->Value(0);
              double a1 = fitResult->Value(1);
              double a2 = fitResult->Value(2);

              std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                  <<" a0 "<<std::setw(10)<<a0<<" a1 "<<std::setw(10)<<a1<<" a2 "<<std::setw(10)<<a2<<std::endl;

              double a = a2;
              double b = -a1/2./a2;
              double c = (4 * a2 * a0 - a1 * a1)/4./a2;

              std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                                              <<" a "<<std::setw(10)<<a<<" b "<<std::setw(10)<<b<<" c "<<std::setw(10)<<c<<std::endl;

              a = round(-a * (1 <<bitShift) );
              b = round(b);
              c = round(c);

              if(a == 0) {
                c = 0;
                std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                                                              <<" a is zero, setting c to 0 as well "<<std::endl;
              }

              std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                                              <<" a "<<std::setw(10)<<a<<" b "<<std::setw(10)<<b<<" c "<<std::setw(10)<<c<<std::endl;

              TF1* intFit = new TF1("intFit","[2]*(x-[1])*(x-[1])+[0]", -100, 1200);

              intFit->SetParameter(2, (-1) * a / (1<<bitShift));
              intFit->SetParameter(1, b);
              intFit->SetParameter(0, c);

              coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(2) = a;
              coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(1) = b;
              coefficients.at(iLayer).at(iEtaBin).at(iRefLayer).at(ptBin).at(0) = c;


              intFit->SetLineColor(kGreen);
              pdfHistInPtBin->GetListOfFunctions()->Add(intFit);
            }
            else {
              std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                                <<" - fit failed!!!!!!!!!!!!!!!!!! "<<std::endl;
            }
          }
          catch (std::exception& err) {
            std::cout<<__FUNCTION__<<": "<<__LINE__<<" iLayer "<<iLayer<<" iEtaBin "<<iEtaBin<<" iRefLayer "<<iRefLayer<<" ptBin "<<ptBin
                                 <<" - fit failed "<<err.what()<<std::endl;
          }

          pdfHistInPtBin->Write();
        }
      }
    }
  }
}
