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
########################################################################################################################


def first_country(df):
    first_c = df.iloc[0, :]
    return first_c
########################################################################################################################


def gold_medal(df):
    return df.iloc[:146, 2].idxmax()
########################################################################################################################


def biggest_difference_in_gold_medal(df):
    return (df.iloc[0:146, 2] - df.iloc[0:146, 6]).argmax()
########################################################################################################################


def get_points(df):
    df['points'] = 3 * (df['Gold'].sum(axis=1)) + 2 * (df['Silver'].sum(axis=1)) + 1 * (df['Bronze'].sum(axis=1))
    return df.iloc[:, 14]
########################################################################################################################


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
########################################################################################################################


########################################################################################################################

#Q1
path="C:/Users/Abhishek Patil/Desktop/Olympics_Dataset/olympics.csv"
df = load_data(path)
print("Dataset: ",df.head(5))

print("\n\nShape of Data: ",df.shape)
########################################################################################################################


#Q2
print("\n\nFirst Country: ",first_country(df))
########################################################################################################################


#Q3
print("\n\nMost Gold Medals: ",gold_medal(df))
########################################################################################################################


#Q4
print("\n\nBiggest difference between their summer and winter gold medal counts: ", biggest_difference_in_gold_medal(df))
########################################################################################################################


#Q5
print("\n\nPoints of Countries: ",get_points(df))
########################################################################################################################


#Q6
print("\n\nK-means Centres of the 4 Clusters formed: ", kMeans(df))
########################################################################################################################
