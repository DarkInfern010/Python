<?php
fscanf(STDIN, "%[^\n]" ,$nb_restaurant);
$compteur = 1;
$moyenne_max = 0;

if ($nb_restaurant >= 5 && $nb_restaurant <= 500){
	do {
		fscanf(STDIN, "%[^\n]" ,$notes);

		$c_note = explode(" ", $notes);	
		$moyenne = ($c_note[0] + $c_note[1] + $c_note[2]) / 3;
		$moyenne_a = ceil ($moyenne);

		if ($moyenne_a > $moyenne_max) {
			$moyenne_max = $moyenne_a;
		}

		$compteur++;

	} while ($compteur <= $nb_restaurant);

	echo "$moyenne_max \n";

}

?>