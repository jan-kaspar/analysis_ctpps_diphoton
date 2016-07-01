import root;
import pad_layout;

string topDir = "../../";

string datasets[] = { "EE", "EB" };

xSizeDef = 10cm;
ySizeDef = 8cm;

xTicksDef = LeftTicks(100., 50.);

//----------------------------------------------------------------------------------------------------

for (string dataset : datasets)
{
	NewPad("diphoton mass$\ung{GeV}$");

	draw(RootGetObject(topDir+dataset+"/distributions.root", "h_dp_mass"), "vl", blue, "selected events");
	draw(RootGetObject(topDir+dataset+"/distributions.root", "h_dp_mass_tr_both_arms"), "vl", red, "selected events with RP tracks L \& R");

	AttachLegend(dataset);
}
