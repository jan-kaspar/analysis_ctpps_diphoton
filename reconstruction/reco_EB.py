import FWCore.ParameterSet.Config as cms

process = cms.Process("Reco")

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
    statistics = cms.untracked.vstring(),
    destinations = cms.untracked.vstring('cout'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING')
    )
)

# raw data source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_1.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_10.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_11.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_12.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_13.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_14.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_15.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_16.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_17.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_18.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_19.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_2.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_20.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_21.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_22.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_23.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_24.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_25.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_26.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_27.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_28.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_29.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_3.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_30.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_31.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_32.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_33.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_34.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_35.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_36.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_37.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_38.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_39.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_4.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_40.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_41.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_5.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_6.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_7.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_8.root',
        '/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EBHighR9/DoubleEG/HighMassDiphoton_EBHighR9/160705_151437/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EBHighR9_9.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# raw-to-digi conversion
process.load("EventFilter.TotemRawToDigi.totemRawToDigi_cff")

# local RP reconstruction chain with standard settings
process.load("RecoCTPPS.Configuration.recoCTPPS_cff")

process.dump = cms.EDAnalyzer("EventContentAnalyzer")

process.p = cms.Path(
    process.totemTriggerRawToDigi *
    process.totemRPRawToDigi *
    process.recoCTPPS
)

# output configuration
from RecoCTPPS.Configuration.RecoCTPPS_EventContent_cff import RecoCTPPSRECO
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("file:./reco_EB.root"),
    outputCommands = RecoCTPPSRECO.outputCommands
)

process.outpath = cms.EndPath(process.output)
