import root;
import pad_layout;

string topDir = "../../";

string datasets[] = { "EE", "EB" };

xSizeDef = 8cm;
ySizeDef = 6cm;

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
	limits((0, 0), (0.25, 3));

	AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$m_{RP}\ung{GeV}$");
	draw(RootGetObject(f, "h_m"), "vl", magenta);
	limits((0, 0), (2000, 4));

	//AttachLegend();
}

NewRow();

for (string dataset : datasets)
{
	string f = topDir+dataset+"/distributions.root";
	
	NewPad("$m_{CMS}\ung{GeV}$", "$m_{RP}\ung{GeV}$");
	draw(RootGetObject(f, "g_m_RP_vs_m_CMS"), "p", heavygreen, mCi+2pt+heavygreen);
	limits((0, 0), (2000, 2000));

	//AttachLegend();
}
