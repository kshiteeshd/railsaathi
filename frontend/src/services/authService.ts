export interface RegisterData {
  full_name: string;
  email: string;
  phone: string;
  password: string;
}

// Base URL comes from frontend/.env (VITE_API_URL).
// Falls back to local backend so `npm run dev` works out of the box.
const API_BASE_URL =
  import.meta.env.VITE_API_URL?.replace(/\/$/, "") ??
  "http://127.0.0.1:8000";

export async function registerUser(data: RegisterData) {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/register`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.detail || "Registration failed.");
    }

    return result;
  } catch (error) {
    if (error instanceof TypeError) {
      throw new Error("Unable to connect to the Rail Saathi server.", {
        cause: error,
      });
    }

    throw error;
  }
}

export interface LoginData {
  email: string;
  password: string;
}

export async function loginUser(data: LoginData) {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.detail || "Login failed.");
    }

    return result;
  } catch (error) {
    if (error instanceof TypeError) {
      throw new Error("Unable to connect to the Rail Saathi server.", {
        cause: error,
      });
    }

    throw error;
  }
}
