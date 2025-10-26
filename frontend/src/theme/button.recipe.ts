import { defineRecipe } from "@chakra-ui/react"

export const buttonRecipe = defineRecipe({
  base: {
    fontWeight: "600",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    transition: "all 0.2s ease",
    borderRadius: "6px",
  },
  variants: {
    variant: {
      solid: {
        bg: { base: "orange.500", _dark: "orange.400" },
        color: { base: "white", _dark: "gray.900" },
        _hover: {
          bg: { base: "orange.600", _dark: "orange.500" },
          transform: "translateY(-1px)",
          boxShadow: "0 4px 12px rgba(242, 159, 103, 0.3)",
        },
        _active: {
          transform: "translateY(0)",
        },
      },
      ghost: {
        bg: "transparent",
        color: { base: "gray.800", _dark: "gray.100" },
        _hover: {
          bg: { base: "gray.100", _dark: "whiteAlpha.100" },
          color: { base: "orange.600", _dark: "orange.400" },
        },
      },
      outline: {
        bg: "transparent",
        borderWidth: "1px",
        borderColor: { base: "gray.200", _dark: "whiteAlpha.300" },
        color: { base: "gray.800", _dark: "gray.100" },
        _hover: {
          borderColor: { base: "orange.500", _dark: "orange.400" },
          color: { base: "orange.600", _dark: "orange.400" },
          bg: { base: "gray.50", _dark: "whiteAlpha.50" },
        },
      },
    },
  },
})
