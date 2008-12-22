import FWCore.ParameterSet.Config as cms
from Configuration.GenProduction.PythiaUESettings_cfi import *





source = cms.Source("PythiaSource",
    pythiaPylistVerbosity = cms.untracked.int32(12),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.untracked.double(10000.0),
    crossSection = cms.untracked.double(0.001906),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(

        pythiaUESettingsBlock,
        processParameters = cms.vstring('PMAS(347,1)=900.0        !mass of RS Graviton',
            'MSEL=0                  !(D=1)',
            'PARP(50) = 0.379  ! Dimensionless coupling constant for RS G*',
            'MSTJ(41)=1              !Switch off Pythia QED bremsshtrahlung',
            'MSUB(391)=1             !',
            'MSUB(392)=1             !',
            '5000039:ALLOFF           ',
            '5000039:ONIFMATCH 23 23  ',
            '23:ALLOFF                ',
            '23:ONIFANY 13 15         '),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters')
    )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1. %'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA6_Exotica_RS1GravitonZZ4Mu_900GeV_007_cff.py,v $'),
    annotation = cms.untracked.string('default documentation string for PYTHIA6_Exotica_RS1GravitonZZ4Mu_900GeV_007_cff.py'),
)