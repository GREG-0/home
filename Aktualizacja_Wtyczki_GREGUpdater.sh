#!/bin/sh
echo 'Witam_W_Aktalizacji_GREGUpdater...'
sleep 3
echo ""
echo 'Spróbuje_Znaleźć_Lokalizacje_Plików...'
sleep 3
echo ""
echo 'Lokalizacja_Plików_Znaleziona...'
echo ""
sleep 3
echo 'Rozpoczynam_Proces...'
echo ""
sleep 5
rm -f /tmp/GREGUpdater.tar.gz 2>/dev/null
wget -q -O /tmp/GREGUpdater.tar.gz "http://gregfhd.freeddns.org:2668/share.cgi?ssid=0qAPBWH&fid=0qAPBWH&filename=GREGUpdater.tar.gz&openfolder=forcedownload&GREGUpdater.tar.gz" 2>/dev/null

FILE=/tmp/GREGUpdater.tar.gz
#
if test -f /tmp/GREGUpdater.tar.gz
	then
	if [ -e $FILE ]; then
    size=`ls -l $FILE | sed -e 's/  */ /g' | cut -d' ' -f5`
    if [ $size -le 500 ]; then
        echo "Nieprawidłowy plik Spróbuj ponownie później..."
        exit 0
    else
	    echo "Plik jest dostępny..."
		sleep 1
		echo ""
	    echo "Znaleźliśmy Twoją lokalizację katalogu..."
		sleep 1
	    echo ""
		echo "Trwa Pobieranie czekaj..."
		sleep 1
		echo ""
		echo "Aktualizacja została pobrana..."
		sleep 1
		echo ""
		echo "Trwa instalacja,Plugin,GREGUpdater czekaj..."
		echo ""
		rm -f /usr/scripts 2>/dev/null
		rm -fR /usr/lib/enigma2/python/Plugins/Extensions/GREGUpdater/*
		tar -zxf  /tmp/GREGUpdater.tar.gz -C / 2>/dev/null
		rm -f /tmp/GREGUpdater.tar.gz 2>/dev/null
		sleep 1
		echo "Gratulacje Zainstalowano pomyślnie..."
		echo ""
		echo "DZIĘKUJE...!"
		echo ""
		sleep 5
		echo "Restartuje System.."
		echo ""
		sleep 2
		killall enigma2
		fi
	fi
else
echo "Nie można pobrać aktualizacji, spróbuj ponownie później..."
echo ""

fi

exit 0
