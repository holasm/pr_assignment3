<?php 

$filename = './test.json';

$file = fopen($filename, "r");

$filesize = filesize( $filename );

$filedata = fread($file, $filesize);

var_dump(json_decode($filedata));

// if(($filetext = fgets($file)) == true ){
//   print $filetext;
// }


fclose( $file );

 ?>