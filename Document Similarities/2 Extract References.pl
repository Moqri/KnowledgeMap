use 5.010;use strict;use warnings;use Text::ParseWords;

open my $fh, '<', '03 Bascket_of_8 2005-2014 Documents - Non-Empty Abstracts.txt' or die $!;
open (OUT, '>05 Bascket_of_8 2005-2014 Documents - Non-Empty Abstracts - References.txt') or die "dead";


my @fields;
while (<$fh>) {
    chomp;
    @fields = split /\t/;
    my $ref = $fields[29]; $ref=~s/"//g;
    my $wos = $fields[58];
    if ($wos ne 'UT'){
        printf  OUT "$wos\t$ref\n";
    }
}
