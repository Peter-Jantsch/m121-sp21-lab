test = {
  'name': 'q41',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(above_eight) == tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> above_eight.num_rows == 43
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure your columns are in the right order!;
          >>> # First column should be 'Title', second column should be 'Rating';
          >>> print(above_eight.sort(0).take([19]))
          Title         | Rating
          Interstellar  | 8.6
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
