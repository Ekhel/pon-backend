# PON Backend Administrator
-------------------------------------------------------------------

![PON](https://lh3.googleusercontent.com/cvi7TL-1kRNgirpHUkzrpxb7X80EdCOrq8t38yTRY3vqQMMgzHo3xk_QEArH7iqqZA6i5O6L5e5mn4Nq7sg0k9Y2edAAfBFph2j_0agfqpR2o-qe51eGF8dPYTOyrQJeEsNy8etA-UtcII6w2KD6x3qdRaPy-YSnOv1sZT7PvTLZ1i1tJvJXv1as9JITwzoCziExXwEunDFLFF1gOyZwlRQi5e9Yd5J8xVkzkF3O5bPbTspJ9_KCSR7k1Wl6mMlMST3vb_UMl9jLz3d48op_si5-X9jSjiMZg_VrZGiOPlHGdpyn-vk3dhdpay744V5fw3L1d5WFArLVIvBxqt4ngSkQCd5vn-2lL2Kmf1QR9zc1PMbTunfDvywP8UzVJM4uR7-lpRJ7bBACCT5RyxYkJDkW1TqT07VY4oPEKzyPhHcPkaYTAVBngth2_zJYV2fSaKgE-JgnldiJnqObQQcEUBnq27lS6W5SMKnLbTis6QyHjGDbyjFV9zAVyb9B-q_QdPO_v5OXMPsm3_Z5l1xtv1uTci7FlMbMG0vdMR1Zi_PTawZa5K3mt_HthoqxmpHjhQbWp27jpV9zEq-zMKM74ENf_NzKmjnBQgUMKcldaeBpwrhDKk9RaiAOU8fAsyElGw2Erecf-LvVfVbd8Ep2dWrM9geMCrqPyoyRv1q91jnpJN6ZS15qQag=w1830-h273-no)

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

