test = {
  'name': 'q31',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> stats = compute_statistics(full_data);
          >>> plt.close();
          >>> plt.close();
          >>> round(float(stats[0]), 2) == 25.85
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> stats = compute_statistics(full_data);
          >>> plt.close();
          >>> plt.close();
          >>> round(float(stats[1]), 2) == 8708058.68
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
