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
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_1.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_2.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_3.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_4.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_5.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_6.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_7.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_8.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_9.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_10.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_11.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_12.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_13.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_14.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_15.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_16.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_17.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_18.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_19.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_20.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_21.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_22.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_23.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_24.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_25.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_26.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_27.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_28.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_29.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_30.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_31.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_32.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_33.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_34.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_35.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_36.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_37.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_38.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_39.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_40.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_41.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_42.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_43.root',
        '/store/group/phys_higgs/cmshgg/lforthom/pickevents/EE/DoubleEG/pickevents_EE/160623_133538/0000/pickevents_44.root'
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
    fileName = cms.untracked.string("file:./reco_EE.root"),
    outputCommands = RecoCTPPSRECO.outputCommands
)

process.outpath = cms.EndPath(process.output)
