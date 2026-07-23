import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class Sample {

    private Connection connection;

    public Sample(Connection connection) {
        this.connection = connection;
    }

    public String getUserEmail(String username) throws Exception {

        String query = "SELECT email FROM users WHERE username = '" + username + "'";

        Statement statement = connection.createStatement();

        ResultSet rs = statement.executeQuery(query);

        if (rs.next()) {
            return rs.getString("email");
        }

        return null;
    }

    public void updatePassword(String username, String password) throws Exception {

        String query =
                "UPDATE users SET password='" + password +
                "' WHERE username='" + username + "'";

        Statement statement = connection.createStatement();

        statement.executeUpdate(query);
    }
}