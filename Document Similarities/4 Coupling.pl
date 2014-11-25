use 5.010;use strict;use warnings;use Text::ParseWords;

chdir 'C:/Users/moqri/Desktop'; 

open my $fh, '<', '07 One Reference Per Line.txt' or die $!;
open (OUT, '>', '09 Couplings.csv') or die "dead";

my @all;
my $line=0;
while (<$fh>) {
    my @tok=split(/\t/);
    $all[$line][0]= $tok[0];     $all[$line][1]=  $tok[1];  
    $line++;
}
my$filesize=$line;
my @count;

for(my$i=0;$i<2500;$i++){for(my$j=$i+1;$j<2500;$j++){$count[$i][$j]=0;}}

for (my $i=0;$i<$filesize;$i++){
    say $i;
    for (my $j=$i+1;$j<$filesize ;$j++){
        if ($all[$i][1] eq $all[$j][1]){
            #say $all[$i][1];
            $count[int($all[$i][0])][int($all[$j][0])]++;
        }
    }
}
for(my$i=0;$i<2500;$i++){for(my$j=$i+1;$j<2500;$j++){
    if ($count[$i][$j]!=0){
        printf OUT "$i,$j,$count[$i][$j]\n";
        }
    }
}
        



    


