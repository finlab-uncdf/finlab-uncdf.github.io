//var hide_empty_list=true; //uncomment this line to hide empty selection lists
var disable_empty_list=true; //uncomment this line to disable empty selection lists

var onclickaction="alert" //set to "alert" or "goto". Former is for debugging purposes, to tell you the value of the final selected list that will be used as the destination URL. Set to "goto" when below configuration is all set up as desired. 

var newwindow=0 //Open links in new window or not? 1=yes, 0=no.

/////DEFINE YOUR MENU LISTS and ITEMS below/////////////////

addListGroup("chainedmenu", "First-Select");

addOption("First-Select", "Select an item", "", 1); //HEADER OPTION
addList("First-Select", "5 days", "", "f");
addList("First-Select", "1 month", "", "o");
addList("First-Select", "3 months", "", "t");

//5-DAYS
addOption("f", "Select an item", "", 1); //HEADER OPTION
addList("f", "Aspiring Entrepreneurs", "", "f-asp");
addList("f", "Early Stage Startups", "", "f-est");
addList("f", "Growth Stage Companies", "", "f-gsc");

//5-DAYS––Aspiring Entrepreneurs
addOption("f-asp", "Select an item", "", 1); //HEADER OPTION
addOption("f-asp", "Innovation Competition", "f-asp");
addOption("f-asp", "Startup Accelerator", "f-asp");
addOption("f-asp", "Training Workshop", "f-asp");

//5-DAYS––Early Stage Startups
addOption("f-est", "Select an item", "", 1); //HEADER OPTION
addOption("f-est", "Innovation Competition", "f-asp");
addOption("f-est", "Startup Accelerator", "f-asp");
addOption("f-est", "Training Workshop", "f-asp");

//5-DAYS––Growth Stage Companies
addOption("f-gsc", "Select an item", "", 1); //HEADER OPTION
addOption("f-gsc", "Innovation Competition", "f-asp");
addOption("f-gsc", "Startup Accelerator", "f-asp");
addOption("f-gsc", "Training Workshop", "f-asp");

//1-MONTH
addOption("o", "Select an item", "", 1); //HEADER OPTION
addList("o", "Aspiring Entrepreneurs", "", "o-asp");
addList("o", "Early Stage Startups", "", "o-est");
addList("o", "Growth Stage Companies", "", "o-gsc");

//1-MONTH––Aspiring Entrepreneurs
addOption("o-asp", "Select an item", "", 1); //HEADER OPTION
addOption("o-asp", "Innovation Competition", "f-asp");
addOption("o-asp", "Startup Accelerator", "f-asp");
addOption("o-asp", "Training Workshop", "f-asp");

//1-MONTH––Early Stage Startups
addOption("o-est", "Select an item", "", 1); //HEADER OPTION
addOption("o-est", "Innovation Competition", "f-asp");
addOption("o-est", "Startup Accelerator", "f-asp");
addOption("o-est", "Training Workshop", "f-asp");

//1-MONTH––Growth Stage Companies
addOption("o-gsc", "Select an item", "", 1); //HEADER OPTION
addOption("o-gsc", "Innovation Competition", "f-asp");
addOption("o-gsc", "Startup Accelerator", "f-asp");
addOption("o-gsc", "Training Workshop", "f-asp");

//3-MONTHS
addOption("t", "Select an item", "", 1); //HEADER OPTION
addList("t", "Aspiring Entrepreneurs", "", "t-asp");
addList("t", "Early Stage Startups", "", "t-est");
addList("t", "Growth Stage Companies", "", "t-gsc");

//3-MONTHS––Aspiring Entrepreneurs
addOption("t-asp", "Select an item", "", 1); //HEADER OPTION
addOption("t-asp", "Innovation Competition", "f-asp");
addOption("t-asp", "Startup Accelerator", "f-asp");
addOption("t-asp", "Training Workshop", "f-asp");

//3-MONTHS––Early Stage Startups
addOption("t-est", "Select an item", "", 1); //HEADER OPTION
addOption("t-est", "Innovation Competition", "f-asp");
addOption("t-est", "Startup Accelerator", "f-asp");
addOption("t-est", "Training Workshop", "f-asp");

//3-MONTHS––Growth Stage Companies
addOption("t-gsc", "Select an item", "", 1); //HEADER OPTION
addOption("t-gsc", "Innovation Competition", "f-asp");
addOption("t-gsc", "Startup Accelerator", "f-asp");
addOption("t-gsc", "Training Workshop", "bad-iead");




