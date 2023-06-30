

from db_utils import close_db_connection, establish_db_connection, read_from_db


def get_last_held_year(format):
    try:
        query = " SELECT MAX(tt.year) year FROM tb_tournaments tt INNER JOIN tb_format tf ON tt.format_id = tf.format_id WHERE tf.format_name=?"
        
        rows = read_from_db(query, format)
        if rows:
            last_year=rows.year
            
            return last_year
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None
    
def get_first_held_year(format):
    try:
        query = " SELECT MIN(tt.year) year FROM tb_tournaments tt INNER JOIN tb_format tf ON tt.format_id = tf.format_id WHERE tf.format_name=?"
        
        rows = read_from_db(query, format)
        if rows:
            first_year=rows.year
            
            return first_year
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None

def get_tournaments(format=None):

    try:
        if format:
            query = "SELECT t.tournament_name  FROM tb_tournaments t INNER JOIN tb_format f ON t.format_id=f.format_id WHERE f.format_name=? order by t.year"
            rows = read_from_db(query, format)
        else:
            query = "SELECT t.tournament_name  FROM tb_tournaments t INNER JOIN tb_format f ON t.format_id=f.format_id order by t.year"
            rows = read_from_db(query)

        
        if rows:
            # Process the fetched details
            # ...
            
            details_list = []
            for row in rows:
                # Assuming each row is a list of values
                details_list.append(row.tournament_name)
            
            return details_list
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None
    
def get_teams():
    query = " SELECT tt.team_name FROM tb_teams tt"
    try:
        rows = read_from_db(query)
        if rows:
            # Process the fetched details
            # ...
            
            details_list = []
            for row in rows:
                # Assuming each row is a list of values
                details_list.append(row.team_name)
            
            return details_list
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None
    
def get_player_of_the_series(format, year):

    try:
        if str(year).upper=="LAST":
            year=get_last_held_year(format)
        elif str(year).upper=="FIRST":
            year=get_first_held_year(format)

        query = " SELECT tt.man_of_the_series FROM tb_tournaments tt INNER JOIN tb_format tf ON tt.format_id = tf.format_id WHERE tf.format_name=? AND tt.year=?"
        parameters = (format,year)
        rows = read_from_db(query, *parameters )
        if rows:

            player=rows[0].man_of_the_series
            
            return player
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None
    
def get_tournaments_years(format):

    try:
        query = " SELECT tt.year FROM tb_tournaments tt INNER JOIN tb_format tf ON tt.format_id = tf.format_id WHERE tf.format_name=?"
        rows = read_from_db(query, format)
        if rows:
            # Process the fetched details
            # ...
            
            details_list = []
            for row in rows:
                # Assuming each row is a list of values
                details_list.append(row.year)
            
            return details_list
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None
    
 
def get_winning_team_of_the_series(format, year):

    try:
        if str(year).upper=="LAST":
            year=get_last_held_year(format)
        elif str(year).upper=="FIRST":
            year=get_first_held_year(format)

        query = " SELECT tm.team_name FROM tb_tournaments tt INNER JOIN tb_format tf ON tt.format_id = tf.format_id INNER JOIN tb_teams tm ON tm.team_id = tt.winner WHERE tf.format_name=? AND tt.year=?"
        parameters= (format,year)
        rows = read_from_db(query, *parameters )
        if rows:

            team=rows[0].team_name
            
            return team
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None

def get_runnerup_of_the_series(format, year):

    try:
        if str(year).upper=="LAST":
            year=get_last_held_year(format)
        elif str(year).upper=="FIRST":
            year=get_first_held_year(format)

        query = " SELECT tm.team_name FROM tb_tournaments tt INNER JOIN tb_format tf ON tt.format_id = tf.format_id INNER JOIN tb_teams tm ON tm.team_id = tt.runner_up WHERE tf.format_name=? AND tt.year=?"
        parameters= (format,year)
        rows = read_from_db(query, *parameters )
        if rows:

            team=rows[0].team_name
            
            return team
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None

def get_most_wickets_taker_of_the_series(format, year):

    try:
        if str(year).upper=="LAST":
            year=get_last_held_year(format)
        elif str(year).upper=="FIRST":
            year=get_first_held_year(format)

        query = " SELECT tt.most_wickets FROM tb_tournaments tt INNER JOIN tb_format tf ON tt.format_id = tf.format_id WHERE tf.format_name=? AND tt.year=?"
        parameters= (format,year)
        rows = read_from_db(query, *parameters )
        if rows:

            player=rows[0].most_wickets
            
            return player
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None
           
def get_most_runs_scorer_of_the_series(format, year):

    try:
        if str(year).upper=="LAST":
            year=get_last_held_year(format)
        elif str(year).upper=="FIRST":
            year=get_first_held_year(format)

        query = " SELECT tt.most_runs FROM tb_tournaments tt INNER JOIN tb_format tf ON tt.format_id = tf.format_id WHERE tf.format_name=? AND tt.year=?"
        parameters= (format,year)
        rows = read_from_db(query, *parameters )
        if rows:

            player=rows[0].most_runs
            
            return player
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None
     
def get_host_of_the_series(format, year):

    try:
        if str(year).upper=="LAST":
            year=get_last_held_year(format)
        elif str(year).upper=="FIRST":
            year=get_first_held_year(format)

        query = "SELECT hs.[host_name] FROM tb_tournaments tt INNER JOIN tb_format tf ON tt.format_id = tf.format_id INNER JOIN tb_host hs ON hs.[host_id] = tt.hosting_id WHERE tf.format_name=? AND tt.year=?"
        parameters= (format,year)
        rows = read_from_db(query, *parameters )
        if rows:

            host=rows[0].host_name
            
            return host
        else:
            print("No details found.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching details: {str(e)}")
        return None
     