import root;
import pad_layout;

string topDir = "../../";

string datasets[] = { "EE", "EB" };

xSizeDef = 10cm;
ySizeDef = 8cm;

//xTicksDef = LeftTicks(100., 50.);

//----------------------------------------------------------------------------------------------------

for (string dataset : datasets)
{
	NewPad(false);
	label("{\SetFontSizesXX " + dataset + "}");
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$\xi$");
	draw(RootGetObject(f, "h_xi_L"), "vl", blue, "left arm");
	draw(RootGetObject(f, "h_xi_R"), "vl", red, "right arm");
	xlimits(0, 0.25, Crop);

	AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$m_{RP}\ung{GeV}$");
	draw(RootGetObject(f, "h_m"), "vl", magenta);
	xlimits(0, 2000, Crop);

	//AttachLegend();
}

NewRow();

TGraph_errorBar = None;

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$m_{CMS}\ung{GeV}$", "$m_{RP}\ung{GeV}$");
	draw((0, 0)--(2000, 2000), dotted);
	draw(RootGetObject(f, "g_m_RP_vs_m_CMS"), "p", heavygreen, mCi+3pt+heavygreen);
	limits((0, 0), (2000, 2000));

	//AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";

	NewPad("diphoton mass$\ung{GeV}$");

	RootGetObject(f, "h_dp_mass");
	draw(robj, "vl", blue, format("diphoton cut (%.0f events)", robj.rExec("GetEntries")));

	RootGetObject(f, "h_dp_mass_tr_both_arms");
	draw(robj, "vl", red, format("diphoton cut, RP tracks L \& R (%.0f events)", robj.rExec("GetEntries")));
	
	AttachLegend();
}
