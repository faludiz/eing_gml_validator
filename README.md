# E-ING GML Validator

E-ING GML formátum ellenőrző program

## Beállítások

Az XSD fájl elérési útvonalát az `eing_gml_validator.ini` fájban kell megadni:

```ini
[eing_gml_validator]

xsd = EING_GML_szabvany_leiras_2.3.xsd  
```

## Használat

### Windows

Az ellenőrzéshez csak húzd és ejtsd az asztali ikonra a GML fájlt.

A beállítások a program asztali ikonjára dupla kattintással érhetők el.

### Parancsorból

```commandline
validate.py gml-file
```

Ahol: `gml-file`: az ellenőrizendő GML fájl

Paraméter nélküli indítás esetén az `eing_gml_validator.ini` fájlt nyitja meg.

### Eredmény

A vizsgálat eredményéről egy riport fájl készül `eredeti.gml.txt` néven, amit az ellenőrzés befejeztével meg is nyit a `.txt` formátumhoz társított alakalmazással. 
