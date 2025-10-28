import { createSystem, defaultConfig } from "@chakra-ui/react"
import { buttonRecipe } from "./theme/button.recipe"

export const system = createSystem(defaultConfig, {
  globalCss: {
    html: {
      fontSize: "16px",
    },
    body: {
      fontSize: "0.875rem",
      margin: 0,
      padding: 0,
    },
    ".main-link": {
      color: { base: "orange.600", _dark: "orange.400" },
      fontWeight: "600",
      textDecoration: "none",
      transition: "color 0.2s ease",
      _hover: {
        color: { base: "orange.700", _dark: "orange.500" },
      },
    },
    "@keyframes reveal": {
      from: {
        opacity: 0,
        transform: "translateY(12px)",
      },
      to: {
        opacity: 1,
        transform: "translateY(0)",
      },
    },
    "@media (prefers-reduced-motion: reduce)": {
      "*": {
        animationDuration: "0.01ms !important",
        animationIterationCount: "1 !important",
        transitionDuration: "0.01ms !important",
      },
    },
  },
  theme: {
    tokens: {
      fonts: {
        heading: { value: "'Fraunces', serif" },
        body: { value: "'Commissioner', system-ui, sans-serif" },
        mono: {
          value:
            "'Azeret Mono', ui-monospace, 'SFMono-Regular', 'Menlo', monospace",
        },
      },
      colors: {
        ui: {
          main: { value: "#F29F67" },
        },
      },
    },
    recipes: {
      button: buttonRecipe,
    },
  },
})
