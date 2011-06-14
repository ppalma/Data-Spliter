#!/bin/bash

Hra=$[$(date --utc +%H) - 1]

if [ $Hra -le 9  ]; then
{
	nombreFichero="$( date --utc +%Y%m%d_0$[$(date --utc +%H) - 1])*.gcf"	
}
else
{	
	nombreFichero="$( date --utc +%Y%m%d_$[$(date --utc +%H) - 1])*.gcf"
}
fi

servidor="190.13.181.234"
usuario="estacion ovdas.,2009"

ftp -n << EOF
prompt off
open $servidor
user $usuario
lcd "/home/user/Scream/junte"
cd "/La_Junta/E/"
mput $nombreFichero
quit
EOF

ftp -n << EOF
prompt off
open $servidor
user $usuario
lcd "/home/user/Scream/juntn"
cd "/La_Junta/N/"
mput $nombreFichero
quit
EOF

ftp -n << EOF
prompt off
open $servidor
user $usuario
lcd "/home/user/Scream/juntz"
cd "/La_Junta/Z/"
mput $nombreFichero
quit
EOF

servidor="190.13.135.66"
usuario="user coy"

ftp -n << EOF
prompt off
open $servidor
user $usuario
lcd "/home/user/Scream/junte"
cd "Scream/LaJuntaGCF/E/"
mput $nombreFichero
quit
EOF

ftp -n << EOF
prompt off
open $servidor
user $usuario
lcd "/home/user/Scream/juntn"
cd "Scream/LaJuntaGCF/N/"
mput $nombreFichero
quit
EOF

ftp -n << EOF
prompt off
open $servidor
user $usuario
lcd "/home/user/Scream/juntz"
cd "Scream/LaJuntaGCF/Z/"
mput $nombreFichero
quit
EOF
