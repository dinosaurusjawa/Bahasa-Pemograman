(hai)

---------------------------------------------------------------------------------------------------------
(FIX Large on Laravel (Mysql,Postgress,MariaDB,Api,Dll)


how to fix large file if u push to GitHub limit

cek file 

git add .

git commit 

git push

jika eror cek bagian mana yang large file limit

lakukan git ignore (nano .gitignore)

(git log --online) untuk cek aktivitas commit

git reset --soft HEAD~1/2/3/4/5

git add . (dll_)

selesai.
---------------------------------------------------------------------------------------------------------
jika belum berhasil saat mengikuti Langkah di atas

hapus data yang membuat large file rm -rf (nama file/folder)

git add . (dll_)

cek nano .git

cek nano .git/config 

(bila perlu reset keduanya)

jika eror lakukan keygen di cd / -> cd root -> ssh-keygen
---------------------------------------------------------------------------------------------------------
lakukan mv file jika perlu (mv nama file -> ubah ke)

git clone (ambil dari GitHub)

jika sudah move file cek file (ls)

lakukan mv folder ke folder yang di pindahkan ke file yang awal (mv pert8/ /root/Bahasa-Pemograman atau mv api /root/Bahasa-Pemograman)

masuk ke delam folder yang awal yang sebelumnya folder baru

git add .

git commit -m "(Nama)

git push

jika sudah (hapus folder" yang tidak penting di awal terminal rm -rf)

tambahan untuk (api bash)

masuk ke folder api docker exec -it api bash

-lakukan reset docker (docker compose down / docker comopose up -d --build)

-setelah itu php artisan migrate

-setelah itu php artisan migrate:fresh --seed

git add .

git commit 

git push 
---------------------------------------------------------------------------------------------------------
