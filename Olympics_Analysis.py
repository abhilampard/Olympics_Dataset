import pandas as pd

def load_data(path):
    df=pd.read_csv(path, skiprows=1)
    col_rename = {'Unnamed: 0': 'Country',
                      '01 !': 'Gold',
                      '02 !': 'Silver',
                      '03 !': 'Bronze',
                      '01 !.1': 'Gold',
                      '02 !.1': 'Silver',
                      '03 !.1': 'Bronze',
                      '01 !.2': 'Gold',
                      '02 !.2': 'Silver',
                      '03 !.2': 'Bronze',
                      'Total.1': 'Total'}
    df.rename(columns=col_rename, inplace=True)
    country_names = [x.split('\xc2\xa0(')[0] for x in df.iloc[:, 0]]
    df.set_index(pd.Series(country_names), inplace=True)
    df.iloc[:, 0] = country_names
    df.drop('Total', axis=1, inplace=True)
    return df

def get_points(df):
    df['points'] = 3 * (df['Gold'].sum(axis=1)) + 2 * (df['Silver'].sum(axis=1)) + 1 * (df['Bronze'].sum(axis=1))
    return df.iloc[:, 14]

def kMeans(df):
    from sklearn.preprocessing import LabelEncoder
    def label_encoder(df, list_of_columns):

        for col in list_of_columns:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col])
        return df

    label_encoder(df, ['Country'])

    from sklearn.cluster import KMeans
    km = KMeans(n_clusters=5, init='k-means++', n_init=10)
    km=km.fit(df)
    return km.cluster_centers_


# Question 1
path="C:/Users/Abhishek Patil/Desktop/Olympics_Dataset/olympics.csv"
df = load_data(path)
print("Dataset: ",df.head(5))
print("\n\nShape of Data: ",df.shape)


# Question 2: Return results for first country
print("\n\nFirst Country: ", df.iloc[0, :])


# Question 3: Return name of country who won most gold medals
print("\n\nMost Gold Medals: ",df.iloc[:146, 2].idxmax())


# Question 4: Return name of country who has biggest difference between their summer and winter gold medal counts
print("\n\nBiggest difference between their summer and winter gold medal counts: ", (df.iloc[0:146, 2] - df.iloc[0:146, 6]).argmax())


# Question 5: Write a function to update the dataframe to include a new column called "Points" for Games which is a weighted value where each gold medal counts for 3 points, silver medals for 2 points, and bronze medals for 1 point. The function should return only the column (a Series object) which you created.
print("\n\nPoints of Countries: ",get_points(df))


# Question 6: Return K-Means cluster centers
print("\n\nK-means Centres of the 4 Clusters formed: ", kMeans(df))
