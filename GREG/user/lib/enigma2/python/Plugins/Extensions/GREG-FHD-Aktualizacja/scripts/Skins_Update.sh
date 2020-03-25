#!/bin/sh

wget -q -O /tmp/GREGORY_FHD_GOLD.tar.gz ftp://grzegorzsliwa.tplinkdns.com/update"("sda1")"/GREGORY_FHD_GOLD.tar.gz 2>/dev/null

if test -f /tmp/GREGORY_FHD_GOLD.tar.gz
then

echo "Aktualizacja została pobrana.."
echo ""
sleep 1
echo "Trwa instalacja, czekaj.."
echo ""
rm -fR /usr/share/enigma2/GREGORY_FHD_GOLD/*
tar -zxf  /tmp/GREGORY_FHD_GOLD.tar.gz -C / 2>/dev/null
rm -f /tmp/ 2>/dev/null
sleep 1
echo "Zainstalowano pomyślnie.."
echo ""
sleep 1
echo "Restartuje Enigme.."
echo ""

sleep 2
killall -9 enigma2 2>/dev/null

else

echo "Nie można pobrać aktualizacji, spróbuj ponownie później.."
echo ""

fi

exit 0
