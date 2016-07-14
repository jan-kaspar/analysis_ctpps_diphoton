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
	draw(RootGetObject(f, "h_xi_L"), "vl", blue+2pt, "left arm");
	draw(RootGetObject(f, "h_xi_R"), "vl", red+2pt, "right arm");
	xlimits(0, 0.25, Crop);

	AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$m_{\rm RP}\ung{GeV}$");
	draw(RootGetObject(f, "h_m"), "vl", magenta+2pt);
	xlimits(0, 2000, Crop);

	//AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$y_{\rm RP}\ung{GeV}$");
	draw(RootGetObject(f, "h_y"), "vl", brown+2pt);
	xlimits(-0.5, 1.0, Crop);

	//AttachLegend();
}

NewRow();

TGraph_errorBar = None;

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$m_{\rm CMS}\ung{GeV}$", "$m_{\rm RP}\ung{GeV}$");
	draw((0, 0)--(2000, 2000), dotted);
	draw(RootGetObject(f, "g_m_RP_vs_m_CMS"), "p", heavygreen, mCi+4pt+heavygreen);
	limits((0, 0), (2000, 2000));

	//AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";

	NewPad("diphoton mass$\ung{GeV}$");

	RootGetObject(f, "h_dp_mass");
	draw(robj, "vl", blue+2pt, format("diphoton cut (%.0f events)", robj.rExec("GetEntries")));

	RootGetObject(f, "h_dp_mass_tr_both_arms");
	draw(robj, "vl", red+2pt, format("diphoton cut, RP tracks L \& R (%.0f events)", robj.rExec("GetEntries")));
	
	AttachLegend();
}
