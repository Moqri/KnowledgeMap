use GD;

my $source = 'C:\Big Perl\Pics';
my $Thumbnail = 'thumb_' . "$source";

my $maxheight = 180;
my $maxwidth = 180;
my $srcimage = GD::Image->new ("$source");

my $newimage = new GD::Image($maxheight,$maxwidth);
$newimage->copyResized($srcimage,0,0,0,0,$maxheight,$maxwidth,180,180);
open(FILE, ">$Thumbnail") || die "Cannot open $Thumbnail : $!\n";
binmode (FILE); 
print FILE $newimage->jpeg;