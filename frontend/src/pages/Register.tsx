import { useState } from "react";
import { registerUser } from "../services/authService";

interface RegisterProps {
  onLogin: () => void;
  showNotification: (
    type: "success" | "error" | "warning" | "info",
    title: string,
    message: string
  ) => void;
}

function Register({
  onLogin,
  showNotification,
}: RegisterProps) {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] =
    useState(false);

  const [isLoading, setIsLoading] = useState(false);

  const [errors, setErrors] = useState<Record<string, string>>({});

  const validateForm = () => {
    const newErrors: Record<string, string> = {};

    const trimmedName = fullName.trim();
    const trimmedEmail = email.trim();
    const trimmedPhone = phone.trim();

    // Full name
    if (!trimmedName) {
      newErrors.fullName = "Full name is required.";
    } else if (trimmedName.length < 2) {
      newErrors.fullName =
        "Full name must contain at least 2 characters.";
    }

    // Email
    if (!trimmedEmail) {
      newErrors.email = "Email is required.";
    }

    // Phone
    if (!trimmedPhone) {
      newErrors.phone = "Phone number is required.";
    } else if (!/^[6-9]\d{9}$/.test(trimmedPhone)) {
      newErrors.phone =
        "Enter a valid 10-digit Indian mobile number.";
    }

    // Password
    if (!password) {
      newErrors.password = "Password is required.";
    } else if (password.length < 8) {
      newErrors.password =
        "Password must contain at least 8 characters.";
    } else if (!/[A-Z]/.test(password)) {
      newErrors.password =
        "Password must contain at least one uppercase letter.";
    } else if (!/[a-z]/.test(password)) {
      newErrors.password =
        "Password must contain at least one lowercase letter.";
    } else if (!/\d/.test(password)) {
      newErrors.password =
        "Password must contain at least one number.";
    } else if (!/[^A-Za-z0-9]/.test(password)) {
      newErrors.password =
        "Password must contain at least one special character.";
    }

    // Confirm password
    if (!confirmPassword) {
      newErrors.confirmPassword =
        "Please confirm your password.";
    } else if (password !== confirmPassword) {
      newErrors.confirmPassword =
        "Passwords do not match.";
    }

    setErrors(newErrors);

    return Object.keys(newErrors).length === 0;
  };

  const handleRegister = async (
    e: React.SubmitEvent<HTMLFormElement>
  ) => {
    e.preventDefault();

    const isValid = validateForm();

    if (!isValid) {
      showNotification(
        "error",
        "Check your details",
        "Please correct the highlighted fields."
      );

      return;
    }

    try {
      setIsLoading(true);

      const result = await registerUser({
        full_name: fullName.trim(),
        email: email.trim(),
        phone: phone.trim(),
        password,
      });

      console.log("Registration successful:", result);

      showNotification(
        "success",
        "Account created",
        "Registration successful. Redirecting to login..."
      );

      // Clear form
      setFullName("");
      setEmail("");
      setPhone("");
      setPassword("");
      setConfirmPassword("");
      setErrors({});

      // Redirect to Login after 3 seconds
      setTimeout(() => {
        onLogin();
      }, 3000);

    } catch (error) {
      const message =
        error instanceof Error
          ? error.message
          : "Something went wrong during registration.";

      showNotification(
        "error",
        "Registration failed",
        message
      );

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
          <h2>Create Account</h2>
          <p>Register to start using Rail Saathi</p>
        </div>

        {/* Form */}
        <form
          onSubmit={handleRegister}
          noValidate
        >

          {/* Full Name */}
          <label htmlFor="fullName">
            Full Name
            <span className="required"> *</span>
          </label>

          <input
            id="fullName"
            type="text"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
            placeholder="Enter your full name"
            autoComplete="name"
            required
            aria-invalid={!!errors.fullName}
          />

          {errors.fullName && (
            <p className="field-error">
              {errors.fullName}
            </p>
          )}


          {/* Email */}
          <label htmlFor="email">
            Email
            <span className="required"> *</span>
          </label>

          <input
            id="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email address"
            autoComplete="email"
            required
            aria-invalid={!!errors.email}
          />

          {errors.email && (
            <p className="field-error">
              {errors.email}
            </p>
          )}


          {/* Phone */}
          <label htmlFor="phone">
            Phone
            <span className="required"> *</span>
          </label>

          <input
            id="phone"
            type="tel"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            placeholder="10-digit mobile number"
            autoComplete="tel"
            inputMode="numeric"
            maxLength={10}
            required
            aria-invalid={!!errors.phone}
          />

          {errors.phone && (
            <p className="field-error">
              {errors.phone}
            </p>
          )}


          {/* Password */}
          <label htmlFor="password">
            Password
            <span className="required"> *</span>
          </label>

          <div className="password-input-wrapper">

            <input
              id="password"
              type={showPassword ? "text" : "password"}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Create a strong password"
              autoComplete="new-password"
              required
              aria-invalid={!!errors.password}
            />

            <button
              type="button"
              className="password-toggle"
              onClick={() =>
                setShowPassword(
                  (previous) => !previous
                )
              }
            >
              {showPassword ? "Hide" : "Show"}
            </button>

          </div>

          <p className="password-hint">
            8+ characters, uppercase, lowercase, number and
            special character.
          </p>

          {errors.password && (
            <p className="field-error">
              {errors.password}
            </p>
          )}


          {/* Confirm Password */}
          <label htmlFor="confirmPassword">
            Confirm Password
            <span className="required"> *</span>
          </label>

          <div className="password-input-wrapper">

            <input
              id="confirmPassword"
              type={
                showConfirmPassword
                  ? "text"
                  : "password"
              }
              value={confirmPassword}
              onChange={(e) =>
                setConfirmPassword(e.target.value)
              }
              placeholder="Confirm your password"
              autoComplete="new-password"
              required
              aria-invalid={!!errors.confirmPassword}
            />

            <button
              type="button"
              className="password-toggle"
              onClick={() =>
                setShowConfirmPassword(
                  (previous) => !previous
                )
              }
            >
              {showConfirmPassword ? "Hide" : "Show"}
            </button>

          </div>

          {errors.confirmPassword && (
            <p className="field-error">
              {errors.confirmPassword}
            </p>
          )}


          {/* Register */}
          <button
            type="submit"
            className="btn btn-primary btn-block"
            disabled={isLoading}
          >
            {isLoading
              ? "Creating Account..."
              : "Register"}
          </button>

        </form>

        {/* Login */}
        <div className="auth-footer">
          <p>
            Already have an account?
            <button
              type="button"
              onClick={onLogin}
            >
              Login
            </button>
          </p>
        </div>

      </div>

    </div>
  );
}

export default Register;