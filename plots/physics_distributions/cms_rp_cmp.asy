import root;
import pad_layout;

string topDir = "../../";

string datasets[];
string dataset_labels[];
datasets.push("2016C"); dataset_labels.push("2016C (EE+EB)");

xSizeDef = 8cm;
ySizeDef = 8cm;

//xTicksDef = LeftTicks(100., 50.);

TGraph_errorBar = None;

//----------------------------------------------------------------------------------------------------

for (int dsi : datasets.keys)
{
	string f = topDir+datasets[dsi]+"/distributions.root";

	NewRow();

	NewPad(false);
	label("{\SetFontSizesXX " + dataset_labels[dsi] + "}");
	
	// mass correlation
	NewPad("$m_{\rm CMS}\ung{GeV}$", "$m_{\rm RP}\ung{GeV}$");
	currentpad.xTicks = LeftTicks(500., 100.);
	currentpad.yTicks = RightTicks(500., 100.);

	draw((0, 0)--(2000, 2000), dashed);
	RootObject g_mass = RootGetObject(f, "g_m_RP_vs_m_CMS");
	draw(g_mass, "p", blue, mCi+3pt+blue);
	limits((0, 0), (2000, 2000));
	
	RootObject g_cand = RootGetObject(f, "g_event_vs_run");

	int N = robj.iExec("GetN");
	for (int i = 0; i < N; ++i)
	{
		real ax[] = {0.};
		real ay[] = {0.};

		g_mass.vExec("GetPoint", i, ax, ay);
		real x = ax[0], y = ay[0];

		g_cand.vExec("GetPoint", i, ax, ay);
		int run = (int) ax[0], event = (int) ay[0];
		
		label(format("%i", (run % 10000)) + format(":%i", (event % 1000)), (x, y), E, blue);
	}
	
	// rapidity correlation
	NewPad("$y_{\rm CMS}\ung{GeV}$", "$y_{\rm RP}\ung{GeV}$");
	//currentpad.xTicks = LeftTicks(500., 100.);
	//currentpad.yTicks = RightTicks(500., 100.);

	draw((-8, -8)--(+8, +8), dashed);
	RootObject g_mass = RootGetObject(f, "g_y_RP_vs_y_CMS");
	draw(g_mass, "p", red, mCi+3pt+red);
	limits((-8, -8), (+8, +8));
	
	RootObject g_cand = RootGetObject(f, "g_event_vs_run");

	int N = robj.iExec("GetN");
	for (int i = 0; i < N; ++i)
	{
		real ax[] = {0.};
		real ay[] = {0.};

		g_mass.vExec("GetPoint", i, ax, ay);
		real x = ax[0], y = ay[0];

		g_cand.vExec("GetPoint", i, ax, ay);
		int run = (int) ax[0], event = (int) ay[0];
		
		label(format("%i", (run % 10000)) + format(":%i", (event % 1000)), (x, y), E, red);
	}
}
