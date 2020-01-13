# PON Backend Administrator
-------------------------------------------------------------------

![PON](https://photos.app.goo.gl/dNMbqGzvqLiKAEzK9)

## System :
* Bahasa Utama :
  - Python

* Framework :
  - Django

* DBMS :
  - SQLite3
  - Postge

* Library :
  - [Requirements.txt](https://github.com/Ekhel/pon-backend/blob/master/requirements.txt)

* Template :
  - ThemeKit v2.0

----------------------------------------------------------------------

## Cara Menggunakan API :
* User Aktif Login Untuk Cek Token
* Register untuk Generate Token


## API Tersedia : (Cloud VPS)
* Auth :
  - [Login](http://194.31.53.36/rest-auth/login/)
  - [Register](http://194.31.53.36/rest-auth/registration/)

* Data Default Router DRF :
  - [API Root](http://194.31.53.36/api/)
  - [API Kota, GET,POST,DELETE,PUT](http://194.31.53.36/api/kota/)
  - [API Kuliner, GET,POST,DELETE,PUT](http://194.31.53.36/api/kuliner/)
  - [API Penginapan, GET,POST,DELETE,PUT](http://194.31.53.36/api/penginapan/)
  - [API Kamar, GET,POST,DELETE,PUT](http://194.31.53.36/api/kamar/)

## API Tersedia : (Cloud Heroku)
* Auth :
  - [Login](https://pon-backend.herokuapp.com/rest-auth/login/)
  - [Register](https://pon-backend.herokuapp.com/rest-auth/registration/)

* Data Default Router DRF :
  - [API Root](https://pon-backend.herokuapp.com/api/)
  - [API Kota, GET,POST,DELETE,PUT](https://pon-backend.herokuapp.com/api/kota/)
  - [API Kuliner, GET,POST,DELETE,PUT](https://pon-backend.herokuapp.com/api/kuliner/)
  - [API Penginapan, GET,POST,DELETE,PUT](https://pon-backend.herokuapp.com/api/penginapan/)
  - [API Kamar, GET,POST,DELETE,PUT](https://pon-backend.herokuapp.com/api/kamar/)


## GraphQL Tersedia : [Graph Editor](https://pon-backend.herokuapp.com/graphql)
  - Schema Kategori kuliner dan Tempat Kuliner

  ```javascript
     {
      allKategori{
        idKk,
        kategori,
        kulinerSet{
          idKuliner,
          title,
          latitude,
          longitude,
          jamBuka,
          jamTutup
        }
      }
    }
  ```

------------------------------------------------------------------------

## Developement :
* Minggu 12/1/2019
  - Tambah Template [Solved]
  - Buat Halaman Login [Solved]
  - Buat Halaman Dashboard [Solved]
  - Buat Halaman Kota, Kuliner, Penginapan [Solved]
  - Deploy Ke Heroku

* Selasa 3 Desember 2019
  - Tambah Layout Kategori Kuliner [Solved]
  - Tambah Layout Item Kuliner [Solved]
  - Tambah Layout kategori Penginapan [Solved]
  - Tambah Layout Item Kamar Pengiapanan [Solved]

