#!usr/bin/perl -w
#use Image::Grab;
use LWP::Simple;

open (FILE, 'AuthorsProfiles11.txt');
$lineno = 1;



while(<FILE>)
{
chomp;
	@profiles = ("ID", "AuthorName", "OfficialWebpage","Affiliation","ResearchFocus","Picture","Notes","email");
	@profiles = split("\t");
	print "ID: $profiles[0]\n";
	print "AuthorName: $profiles[1]\n";
	print "OfficialWebpage: $profiles[2]\n";
	print "Affiliation: $profiles[3]\n";
	print "ResearchFocus: $profiles[4]\n";
	print "Picture: $profiles[5]\n";	
	print "Notes: $profiles[6]\n";
	print "email: $profiles[7]\n";
	print "---------";
	print $lineno++;
my $url = $profiles[5]; 
my $file = $profiles[0].".jpg"; 

getstore($url, $file);
	}

	

