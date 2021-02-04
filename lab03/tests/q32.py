test = {
  'name': 'q32',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(imdb) == tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> imdb.num_rows == 250
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> imdb.select('Votes', 'Rating', 'Title', 'Year', 'Decade').sort(0).take(range(2,5))
          Votes | Rating | Title                | Year | Decade
          50785 | 8.1    | Black Cat, White Cat | 1998 | 1990
          51225 | 8.2    | Sholay               | 1975 | 1970
          51464 | 8.1    | Song of the Sea      | 2014 | 2010
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
