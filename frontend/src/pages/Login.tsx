import { useState } from "react";
import { loginUser } from "../services/authService";

interface LoginProps {
  onRegister: () => void;
  showNotification: (
    type: "success" | "error" | "warning" | "info",
    title: string,
    message: string,
  ) => void;
}

function Login({ onRegister, showNotification }: LoginProps) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [showPassword, setShowPassword] = useState(false);

  const [isLoading, setIsLoading] = useState(false);

  const [errors, setErrors] = useState<{
    email?: string;
    password?: string;
  }>({});

  const validateForm = () => {
    const newErrors: {
      email?: string;
      password?: string;
    } = {};

    if (!email.trim()) {
      newErrors.email = "Email is required.";
    }

    if (!password) {
      newErrors.password = "Password is required.";
    }

    setErrors(newErrors);

    return Object.keys(newErrors).length === 0;
  };

  const handleLogin = async (e: React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();

    const isValid = validateForm();

    if (!isValid) {
      showNotification(
        "error",
        "Check your details",
        "Please enter your email and password.",
      );

      return;
    }

    try {
      setIsLoading(true);

      const result = await loginUser({
        email: email.trim(),
        password,
      });

      localStorage.setItem("access_token", result.access_token);

      showNotification(
        "success",
        "Login successful",
        "Welcome back to Rail Saathi.",
      );

      console.log("Login successful:", result);
    } catch (error) {
      const message =
        error instanceof Error ? error.message : "Unable to login.";

      showNotification("error", "Login failed", message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        {/* Brand */}
        <div className="brand">
          <h1>Rail Saathi</h1>
          <p>Your journey, simplified.</p>
        </div>

        {/* Heading */}
        <div className="auth-heading">
          <h2>Welcome Back</h2>
          <p>Login to your Rail Saathi account</p>
        </div>

        {/* Form */}
        <form onSubmit={handleLogin} noValidate>
          {/* Email */}
          <label htmlFor="loginEmail">
            Email
            <span className="required"> *</span>
          </label>

          <input
            id="loginEmail"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email address"
            autoComplete="email"
            required
            aria-invalid={!!errors.email}
          />

          {errors.email && <p className="field-error">{errors.email}</p>}

          {/* Password */}
          <label htmlFor="loginPassword">
            Password
            <span className="required"> *</span>
          </label>

          <div className="password-input-wrapper">
            <input
              id="loginPassword"
              type={showPassword ? "text" : "password"}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter your password"
              autoComplete="current-password"
              required
              aria-invalid={!!errors.password}
            />

            <button
              type="button"
              className="password-toggle"
              onClick={() => setShowPassword((previous) => !previous)}
            >
              {showPassword ? "Hide" : "Show"}
            </button>
          </div>

          {errors.password && <p className="field-error">{errors.password}</p>}

          {/* Login */}
          <button
            type="submit"
            className="btn btn-primary btn-block"
            disabled={isLoading}
          >
            {isLoading ? "Logging in..." : "Login"}
          </button>
        </form>

        {/* Register */}
        <div className="auth-footer">
          <p>
            Don't have an account?
            <button type="button" onClick={onRegister}>
              Register
            </button>
          </p>
        </div>
      </div>
    </div>
  );
}

export default Login;
