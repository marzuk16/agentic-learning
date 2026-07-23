from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="none",
)

prompt = """
Review the following Java code.

Return valid JSON only.

{
    "summary":"",
    "bugs":[],
    "improvements":[]
}

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class UserService {

    private Connection connection;

    public UserService(Connection connection) {
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
"""

response = client.chat.completions.create(
    model="mlx-community/Qwen3-8B-4bit",
    temperature=0,
    max_tokens=2048,
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)

print(response.choices[0].message.content)