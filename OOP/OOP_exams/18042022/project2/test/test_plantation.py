from project2.plantation import Plantation

from unittest import TestCase

class TestPlantation(TestCase):

    def test_initial_plant_class(self):
        pl = Plantation(5)
        self.assertEqual([], pl.workers)
        self.assertEqual({}, pl.plants)
        self.assertEqual(5, pl.size)
        with self.assertRaises(ValueError) as ex:
            wrong_pl = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ex.exception))
        res1 = pl.hire_worker("pesho")
        self.assertEqual(f"pesho successfully hired.", res1)
        self.assertEqual(['pesho'], pl.workers)
        pl.hire_worker('stamat')
        self.assertEqual(['pesho', 'stamat'], pl.workers)
        with self.assertRaises(ValueError) as ex:
            pl.hire_worker('stamat')
        self.assertEqual("Worker already hired!", str(ex.exception))
        self.assertEqual(0, len(pl))
        res2 = pl.planting('stamat', 'flower1')
        self.assertEqual(f"stamat planted it's first flower1.", res2)
        pl.planting('pesho', 'flower2')
        res3 = pl.planting('pesho', 'flower3')
        self.assertEqual(f"pesho planted flower3.", res3)
        pl.planting('pesho', 'flower4')
        pl.planting('pesho', 'flower5')
        self.assertEqual(5, len(pl))
        self.assertEqual(
            {'pesho': ['flower2', 'flower3', 'flower4', 'flower5'], 'stamat': ['flower1']},
            pl.plants
        )
        with self.assertRaises(ValueError) as ex:
            pl.planting('pesho', 'flower6')
        self.assertEqual("The plantation is full!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            pl.planting('sasho', 'flower6')
        self.assertEqual(f"Worker with name sasho is not hired!", str(ex.exception))

        self.assertEqual('Plantation size: 5\n' + \
                            'pesho, stamat\n' + \
                        'stamat planted: flower1\n' + \
        'pesho planted: flower2, flower3, flower4, flower5', str(pl))

        self.assertEqual('Size: 5\n' + 'Workers: pesho, stamat', repr(pl))









