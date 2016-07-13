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
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_1.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_10.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_11.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_12.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_13.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_14.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_15.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_16.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_17.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_18.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_19.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_2.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_20.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_21.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_22.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_23.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_24.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_25.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_26.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_27.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_28.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_29.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_3.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_30.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_31.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_32.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_33.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_34.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_35.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_36.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_37.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_38.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_39.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_4.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_40.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_41.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_42.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_43.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_44.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_45.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_46.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_47.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_48.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_49.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_5.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_50.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_51.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_52.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_53.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_54.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_55.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_56.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_57.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_58.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_59.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_6.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_60.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_61.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_62.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_63.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_64.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_65.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_66.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_67.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_68.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_69.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_7.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_70.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_71.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_72.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_73.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_74.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_75.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_76.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_77.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_78.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_79.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_8.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_80.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_81.root',
		'/store/group/phys_higgs/cmshgg/lforthom/HighMassDiphoton_EEHighR9/DoubleEG/HighMassDiphoton_EEHighR9/160705_151554/0000/HighMassDiphoton_M500_PtSingle75-EtaSingle2p5_HLTDoublePhoton60-85_EEHighR9_9.root'
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
