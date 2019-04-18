<?php

fscanf(STDIN, "%s", $prix);
fscanf(STDIN, "%s", $tables);
fscanf(STDIN, "%s", $personnes);

$compteur = 0;
$resultat = 0; 

do {
    $prix_tables = $prix * $personnes;
	if ($personnes >= 10) {
		$prix_tables = $prix_tables*0.7;
	} elseif ($personnes >= 6) {
		$prix_tables = $prix_tables*0.8;
	} elseif ($personnes >= 4) {
		$prix_tables = $prix_tables*0.9;
	}
    $resultat += $prix_tables;
	$compteur++;
}while ($compteur <= $tables) ;

echo ceil($resultat);
?>