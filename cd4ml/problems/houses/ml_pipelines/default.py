ml_pipeline_params = {
    'default_algorithm': 'random_forest',
    'acceptance_metric': 'rms_score',
    'acceptance_threshold_min': 0.0,
    'acceptance_threshold_max': 125000,
    'training_random_seed': 4548276,
    'identifier_field': 'sale_id',
    'target_field': 'price',
    'feature_set_name': 'feature_set_1',
    'max_rows_to_read': None,
    'splitting': {
        'random_seed': 1299472653,
        'training_random_start': 0.0,
        'training_random_end': 0.1,
        'validation_random_start': 0.9,
        'validation_random_end': 1.0
    },
    'validation_metric_names': ['r2_score', 'rms_score', 'mad_score', 'num_validated']}
