import pytest
from sqlalchemy import create_engine, text
from Config import config


db_connection_string = config.db_connection_string()
user_id = 99999
email = "test_user@example.com"
new_email = "test_user2026@example.com"
subject_id = 26


@pytest.mark.insert_test
def test_add_user():
    db = create_engine(db_connection_string)
    with db.connect() as connection:

        connection.execute(
            text("DELETE FROM users WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        connection.commit()

        insert_sql = text("""
                          INSERT INTO users (user_id, user_email, subject_id)
                          VALUES (:user_id, :email, :subject_id)
        """)

        connection.execute(insert_sql, {
            "user_id": user_id,
            "email": email,
            "subject_id": subject_id
        })

        connection.commit()

        result = connection.execute(
            text("SELECT user_email FROM users WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        user = result.fetchone()

        assert user is not None
        assert user[0] == email

        connection.execute(
            text("DELETE FROM users WHERE user_id = :user_id"),
            {"user_id": user_id}
        )

    connection.commit()


@pytest.mark.update_test
def test_update_user():
    db = create_engine(db_connection_string)
    with db.connect() as connection:

        connection.execute(
            text("DELETE FROM users WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        connection.commit()

        insert_sql = text("""
                          INSERT INTO users (user_id, user_email, subject_id)
                          VALUES (:user_id, :email, :subject_id)
        """)

        connection.execute(insert_sql, {
            "user_id": user_id,
            "email": email,
            "subject_id": subject_id
        })

        connection.commit()

        update_sql = text("""
                          UPDATE users SET user_email = :email
                          WHERE user_id = :user_id
                          AND subject_id = :subject_id
        """)

        connection.execute(update_sql, {
            "user_id": user_id,
            "email": new_email,
            "subject_id": subject_id
        })

        connection.commit()

        result = connection.execute(
            text("SELECT user_email FROM users WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        user = result.fetchone()

        assert user is not None
        assert user[0] == new_email

        connection.execute(
            text("DELETE FROM users WHERE user_id = :user_id"),
            {"user_id": user_id}
        )

        connection.commit()


@pytest.mark.delete_test
def test_delete_user():
    db = create_engine(db_connection_string)
    with db.connect() as connection:

        connection.execute(
            text("DELETE FROM users WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        connection.commit()

        insert_sql = text("""
                          INSERT INTO users (user_id, user_email, subject_id)
                          VALUES (:user_id, :email, :subject_id)
        """)

        connection.execute(insert_sql, {
            "user_id": user_id,
            "email": email,
            "subject_id": subject_id
        })

        connection.commit()

        result = connection.execute(
            text("SELECT COUNT(*) FROM users WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        count_before = result.scalar()
        assert count_before == 1

        delete_sql = text("""
                          DELETE FROM users
                          WHERE user_id = :user_id AND subject_id = :subject_id
        """)

        connection.execute(delete_sql, {
            "user_id": user_id,
            "subject_id": subject_id
        })

        connection.commit()

        result = connection.execute(
            text("SELECT COUNT(*) FROM users WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        count_after = result.scalar()

        assert count_after == 0
