# Tracklisted

Command line tool that scrapes a Discogs album link and automatically generates a Wikipedia [Track listing](https://en.wikipedia.org/wiki/Template:Track_listing) template.

Note that Discogs is user-generated and is [not considered a reliable source](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources/Perennial_sources#Discogs), so the information should be cross-referenced with other sources. However, this can be a good starting point for creating a Wikipedia track listing.

## Example usage

With the following command:

`python3 tracklisted.py https://www.discogs.com/release/24911627-Kerri-Chandler-Spaces-And-Places`

The output is:

```
{{Track listing
| title1 = Back To Earth (Find Your Peace) (Original Mix) (The Knockdown Center)
| length1 = 7:31
| note1 = feat. Aaron Braxton Jr
| title2 = Never Thought (Main Vocal Mix) (Printworks)
| length2 = 6:17
| note2 = feat. Sunchilde (2)
| title3 = Milan (Full Sax Mix) (Magazzini Generali)
| length3 = 5:59
| note3 = feat. Mauro Capitale
| title4 = You Get Lost In It (Full Vocal Main Mix) (The Warehouse Project)
| length4 = 6:58
| note4 = feat. Lady Linn
| title5 = Hurry Up (Kerri's Again Mix) (Ministry Of Sound)
| length5 = 6:55
| note5 = feat. Dreamer G
| title6 = Tenacity (Main Vocal Mix) (Output)
| length6 = 6:25
| note6 = feat. Bluey Robinson
| title7 = Kaiku (Disco Version) (Kaiku)
| length7 = 6:43
| note7 = feat. Patrick Mangan and Yaniel
| title8 = Industria (Original Mix) (Industria)
| length8 = 8:05
| title9 = Dirty (DJ Deep's Son & Dad Edit) (Rex)
| length9 = 6:58
| note9 = feat. DJ Deep and Leirbag
| title10 = I See (Full Mix) (Razzmatazz)
| length10 = 6:40
| title11 = The Piano Thing (Live) (Original Mix) (Eathos)
| length11 = 7:51
| title12 = Sunrise (Original Mix) (Watergate)
| length12 = 7:15
| title13 = See The Light (Original Long Vocoder Vocal Mix) (Lux Frágil)
| length13 = 8:15
| title14 = Sun Of Sound (Vocal Mix) (Plan B)
| length14 = 8:28
| note14 = feat. Troy Denari
| title15 = Keep One (But Do It Again) (Original Mix) (Sir Henrys)
| length15 = 7:05
| title16 = Who Knows (Media Vocal Mix) (Barbarellas)
| length16 = 6:39
| note16 = feat. Dora Dora
| title17 = Let It (Kerri's Full Vocal Mix) (Basic Club)
| length17 = 5:54
| title18 = Change Your Mind (Full Vocal) (District 8)
| length18 = 9:29
| note18 = feat. Troy Denari
| title19 = Joyful Life (Full Vocal Mix) (De Marktkantine)
| length19 = 6:46
| note19 = feat. Mona Lee (2)
| title20 = The Morning Heat (Main Mix) (La Grange)
| length20 = 8:04
| note20 = feat. Nadir Simon
| title21 = The Calling (Original Mix) (Club Qu)
| length21 = 15:17
| title22 = Feelin' Red (Pull The 9 Out Mix) (DC10)
| length22 = 7:08
| title23 = Subbie (The Jackpot Mix) (Sub Club)
| length23 = 6:55
| title24 = The Box Frame (Original Mix) (Halcyon)
| length24 = 8:22
| total_length = 181:59
}}
```