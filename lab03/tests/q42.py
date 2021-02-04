test = {
  'name': 'q42',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(before_2000 - 8.333088235294117) < 1e-5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> abs(after_or_in_2000 - 8.277192982456139) < 1e-5
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
