test = {
  'name': 'q36',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> wheaton_markets.num_rows == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(wheaton_markets.column('city')) == ['Wheaton', 'Wheaton']
          True
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
