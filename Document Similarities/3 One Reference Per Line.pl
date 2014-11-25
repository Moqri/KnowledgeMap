use 5.010;use strict;use warnings;use Text::ParseWords;

open my $fh, '<', '05 Bascket_of_8 2005-2014 Documents - Non-Empty Abstracts - References.txt' or die $!;
open (OUT, '>', '07 One Reference Per Line.txt') or die "dead";


my @fields;
my$line=0;
while (<$fh>) {
    $line++;
    chomp;
    @fields = split /\t/;   
    my $wos = $fields[0];
    my @ref = split /;/,$fields[1]; 
    foreach (@ref) {
        $_ =~ s/^\s+//;
        printf OUT  "$line\t";
        printf OUT "$_\n"; 
        }
}
