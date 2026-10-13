# TASK 4 — Pagine HTML non in sitemap (classificazione PRE-applicazione di (c))

Sitemap attuale: **75** URL. HTML nel repo: **122**.

| Path | Classe | Motivo |
|---|---|---|
| `de/bergamo/` … `de/sondrio/` (seller refresh, 8) | **(b) rimando** | meta-refresh → IT seller; aggiungere `noindex` |
| `de/haus-kaufen-{bergamo,cremona,lodi,mantova,monza,pavia,sondrio}/` (7) | **(b) rimando** | meta-refresh → EN buyer; aggiungere `noindex` |
| `fr/{bergamo,cremona,lodi,mantova,monza,pavia,sondrio}/` (7) | **(b) rimando** | meta-refresh → IT seller; aggiungere `noindex` |
| `fr/acheter-maison-{bergamo,cremona,lodi,mantova,monza,pavia,sondrio}/` (7) | **(b) rimando** | meta-refresh → EN buyer; aggiungere `noindex` |
| `guida-prezzi-mq-{milano,bergamo,brescia}/` (3) | **(b) rimando** | meta-refresh → VCT; allineare stub + `noindex` |
| `zh/**` (16) | **(d) zh noindex** | restano online, no sitemap, rimuovere link in entrata |
| — | **(a) da aggiungere** | **nessuna** |
| — | **(c) obsolete da trasformare** | **nessuna** (già tutte rimandi o zh) |

**Nota:** nessuna azione (c) da applicare. Si procede con (b)+(d) e i task successivi.
