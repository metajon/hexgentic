import csv
import os
import tempfile
import uuid
from types import SimpleNamespace
from unittest import TestCase

from hexgen.mapgen import MapGen


class TestCsvExport(TestCase):

    def test_export_csv_writes_hex_coordinates_and_contents(self):
        hexagon = SimpleNamespace(
            x=2,
            y=3,
            id=uuid.UUID('12345678-1234-5678-1234-567812345678'),
            altitude=42,
            temperature=(4.5, 8.5),
            moisture=7,
            biome=SimpleNamespace(name='grasslands'),
            type=SimpleNamespace(name='land'),
            is_inland=True,
            is_coast=False,
            geoform=None,
            territory=None,
            features=set(),
            resource=None
        )
        mapgen = MapGen.__new__(MapGen)
        mapgen.hex_grid = SimpleNamespace(hexes=[hexagon])
        mapgen.find_river = lambda x, y: []

        handle, filename = tempfile.mkstemp(suffix='.csv')
        os.close(handle)
        try:
            mapgen.export_csv(filename)
            with open(filename, newline='', encoding='utf-8') as infile:
                rows = list(csv.DictReader(infile))
        finally:
            os.remove(filename)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['x'], '2')
        self.assertEqual(rows[0]['y'], '3')
        self.assertEqual(rows[0]['altitude'], '42')
        self.assertEqual(rows[0]['biome'], 'grasslands')
