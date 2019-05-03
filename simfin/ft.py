import featuretools as ft
from config import *


def ft_dfs(df, prim):
    # Make an entityset and add the entity
    es = ft.EntitySet(id='simfin')
    es.entity_from_dataframe(entity_id='simfin', dataframe=df, make_index=True, index='index')
    fm, fd = ft.dfs(entityset=es, target_entity='simfin', trans_primitives=prim, verbose=True, )
    return fm

top_features = 15
self.orig_df = self.data_df

# Get top important features
self = self.important_features(exclude_regex='Flat_|Price')
data = self.X.loc[:, self.feature_importance.index[:top_features]]
# Feature engineer
data = ft_dfs(data, ['subtract_numeric'])
new_cols = data.columns.difference(self.data_df.columns)
self.data_df = self.data_df.merge(data[new_cols], left_index=True, right_index=True, how='outer')


# Get top important features
self = self.important_features(exclude_regex='Flat_|Price')
data = self.X.loc[:, self.feature_importance.index[:top_features]]
# Feature engineer
data = ft_dfs(data, ['add_numeric'])
new_cols = data.columns.difference(self.data_df.columns)
self.data_df = self.data_df.merge(data[new_cols], left_index=True, right_index=True, how='outer')


top_features = 25

self = self.important_features(exclude_regex='Flat_|Price')
data = self.X.loc[:, self.feature_importance.index[:top_features]]
data = ft_dfs(data, ['divide_numeric'])
new_cols = data.columns.difference(self.data_df.columns)
self.data_df = self.data_df.merge(data[new_cols], left_index=True, right_index=True, how='outer')

fun_df = self.data_df


### Now work with price


top_features = 15
self = self.important_features(include_regex='Price|Flat_')
data = self.X.loc[:, self.feature_importance.index[:top_features]]
data = ft_dfs(data, ['subtract_numeric'])
new_cols = data.columns.difference(self.data_df.columns)
self.data_df = self.data_df.merge(data[new_cols], left_index=True, right_index=True, how='outer')

top_features = 25
self = self.important_features(include_regex='Price|Flat_')
data = self.X.loc[:, self.feature_importance.index[:top_features]]
data = ft_dfs(data, ['divide_numeric'])
new_cols = data.columns.difference(self.data_df.columns)
self.data_df = self.data_df.merge(data[new_cols], left_index=True, right_index=True, how='outer')

price_df = self.data_df


# Combine both fundamental and price
new_cols = fun_df.columns.difference(price_df.columns)
self.data_df = self.data_df.merge(data[new_cols], left_index=True, right_index=True, how='outer')


top_features = 50

self = self.important_features(include_regex='Price|Flat_')
self = self.split()
# data = self.X
data = self.X.loc[:, self.feature_importance.index[:top_features]]
data = ft_dfs(data, ['divide_numeric'])
new_cols = data.columns.difference(self.data_df.columns)
self.data_df = self.data_df.merge(data[new_cols], left_index=True, right_index=True, how='outer')


# Get final important features
self = self.select_features()




