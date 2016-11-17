use 5.010;use strict;use warnings;use Text::ParseWords;use Text::CSV;

chdir 'C:/Users/moqri/Desktop'; 

open my $lsa, '<', '01 LSI - similarities.csv' or die $!;
open my $bib, '<', '02 Couplings.csv' or die $!;

open (OUT, '>', '04 LSI-Bib.csv') or die "dead";

my $csv = Text::CSV->new;
my @bibs;
while( my $row = $csv->getline( $bib ) ) { 
    #shift @$row;        # throw away first value
    push @bibs, $row;
}

my$j=0;
printf OUT "source,target,weight,type\n";
while (<$lsa>) {
    $j++;
    my @tok=split(/\,/);  
    if ($tok[2]>.6){
        printf OUT "$tok[0],$tok[1],$tok[2],$tok[3]";
        print "$j\n";
    }else{    
        foreach my$row (@bibs){
            #<stdin>;
            if (@{$row}[0] eq $tok[0] and @{$row}[1] eq $tok[1]){
                printf OUT "$tok[0],$tok[1],$tok[2],$tok[3]";
                print "$j\n";
                last;           
            }
        }
    }
}


    


