import { Container, Heading, Stack, Text } from "@chakra-ui/react"
import { useTheme } from "next-themes"

import { Radio, RadioGroup } from "@/components/ui/radio"

const Appearance = () => {
  const { theme, setTheme } = useTheme()

  return (
    <Container maxW="full">
      <Heading
        size="sm"
        py={4}
        fontFamily="heading"
        color={{ base: "gray.900", _dark: "gray.100" }}
      >
        Appearance
      </Heading>
      <Text
        fontSize="sm"
        color={{ base: "gray.600", _dark: "gray.400" }}
        mb={4}
      >
        Choose your preferred color theme. The Industrial Editorial theme is
        optimized for dark mode.
      </Text>

      <RadioGroup
        onValueChange={(e) => setTheme(e.value ?? "dark")}
        value={theme}
        colorPalette="orange"
      >
        <Stack>
          <Radio value="dark">Dark Mode (Recommended)</Radio>
          <Radio value="light">Light Mode</Radio>
          <Radio value="system">System</Radio>
        </Stack>
      </RadioGroup>
    </Container>
  )
}
export default Appearance
