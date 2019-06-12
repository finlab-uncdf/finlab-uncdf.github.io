//var hide_empty_list=true; //uncomment this line to hide empty selection lists
var disable_empty_list=true; //uncomment this line to disable empty selection lists

var onclickaction="goto" //set to "alert" or "goto". Former is for debugging purposes, to tell you the value of the final selected list that will be used as the destination URL. Set to "goto" when below configuration is all set up as desired. 

var newwindow=0 //Open links in new window or not? 1=yes, 0=no.

/////DEFINE YOUR MENU LISTS and ITEMS below/////////////////

addListGroup("chainedmenu", "First-Select");

addOption("First-Select", "Select an item", "", 1); //HEADER OPTION
addList("First-Select", "Understand", "", "Understand");//webmaster
addList("First-Select", "Plan", "", "Plan");//news sites
addList("First-Select", "Define", "", "Define");//car sites
addList("First-Select", "Energise", "", "Energise");
addList("First-Select", "Make", "", "Make");
addList("First-Select", "Test", "", "Test");
addList("First-Select", "Improve", "", "Improve");
addList("First-Select", "Ideate", "", "Ideate");

//UNDERSTAND
addOption("Understand", "Select an item", "", 1); //HEADER OPTION
addOption("Understand", "Problem", "tools/ptree.html");
addOption("Understand", "Customers", "http://www.codingforums.com"); //END OF THIS NODE

//PLAN
addOption("Plan", "Select an item", "", 1); //HEADER OPTION
addOption("Plan", "Research", "http://www.codingforums.com");
//addOption("Understand", "Customers", "http://www.codingforums.com"); //END OF THIS NODE

//ENERGISE
addOption("Energise", "Select an item", "", 1); //HEADER OPTION
addOption("Energise", "Self", "http://www.codingforums.com");
addOption("Energise", "Team", "http://www.codingforums.com"); //END OF THIS NODE


//MAKE
addOption("Make", "Select an item", "", 1); //HEADER OPTION
addOption("Make", "Storyboard", "http://www.codingforums.com");
addOption("Make", "Prototype", "http://www.codingforums.com"); //END OF THIS NODE


//TEST
addOption("Test", "Select an item", "", 1); //HEADER OPTION
addOption("Test", "Solutions", "http://www.codingforums.com");
//addOption("Understand", "Customers", "http://www.codingforums.com"); //END OF THIS NODE

//IMPROVE
addOption("Improve", "Select an item", "", 1); //HEADER OPTION
addOption("Improve", "Pitches", "http://www.codingforums.com");
addOption("Improve", "Decks", "http://www.codingforums.com"); //END OF THIS NODE

//IDEATE
addOption("Ideate", "Select an item", "", 1); //HEADER OPTION
addOption("Ideate", "Solutions", "http://www.codingforums.com");
//addOption("Improve", "Decks", "http://www.codingforums.com"); //END OF THIS NODE




