<script>
  import { onMount } from "svelte";

  export let params;

  let squared = 0;

  $: params, fetchNumberDetails();
  async function fetchNumberDetails() {
    const res = await fetch(
      import.meta.env.VITE_API_BASE_URL + `/number/` + params.number
    );
    const data = await res.json();
    squared = data.squared;
  }
</script>

<p>
  Number: {params.number}
</p>

<p>
  Squared: {squared}
</p>
