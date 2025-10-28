import { Box } from "@chakra-ui/react"

export default function AppBackground() {
  return (
    <Box
      position="fixed"
      inset="0"
      pointerEvents="none"
      zIndex="-1"
      overflow="hidden"
    >
      <Box
        position="absolute"
        inset="0"
        bgGradient="to-b"
        gradientFrom={{ base: "#FFFFFF", _dark: "#0B0E12" }}
        gradientTo={{ base: "#F5F5F5", _dark: "#0E1016" }}
      />

      <Box
        position="absolute"
        top="-20%"
        left="-10%"
        width="50%"
        height="50%"
        borderRadius="full"
        bgGradient="radial"
        gradientFrom="rgba(242, 159, 103, 0.08)"
        gradientTo="transparent"
        filter="blur(80px)"
      />

      <Box
        position="absolute"
        top="-10%"
        right="-10%"
        width="40%"
        height="40%"
        borderRadius="full"
        bgGradient="radial"
        gradientFrom="rgba(69, 195, 144, 0.06)"
        gradientTo="transparent"
        filter="blur(80px)"
      />

      <Box
        position="absolute"
        inset="0"
        opacity="0.05"
        mixBlendMode="overlay"
        css={{
          backgroundImage: `
            repeating-linear-gradient(
              0deg,
              rgba(255, 255, 255, 0.03) 0px,
              transparent 1px,
              transparent 40px,
              rgba(255, 255, 255, 0.03) 41px
            ),
            repeating-linear-gradient(
              90deg,
              rgba(255, 255, 255, 0.03) 0px,
              transparent 1px,
              transparent 40px,
              rgba(255, 255, 255, 0.03) 41px
            )
          `,
        }}
      />
    </Box>
  )
}
